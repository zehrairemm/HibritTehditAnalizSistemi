using System;
using System.Diagnostics;
using System.IO;

class Program
{
  
    const string PROJE_YOLU = @"/Users/zehrairemuzunoglu/Desktop/HibritGuvenlik";

    static void Main(string[] args)
    {
        Console.ForegroundColor = ConsoleColor.Green;
        Console.WriteLine("==========================================");
        Console.WriteLine("   HİBRİT TEHDİT ANALİZ SİSTEMİ v1.0");
        Console.WriteLine("==========================================");
        Console.ResetColor();

       
        if (!Directory.Exists(PROJE_YOLU))
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine($"[HATA] Belirtilen klasör bulunamadı:\n{PROJE_YOLU}");
            Console.WriteLine("Lütfen Program.cs içindeki PROJE_YOLU satırını düzeltin.");
            return;
        }

        while (true)
        {
            Console.Write("\n[?] Analiz edilecek metni girin (Çıkış için 'exit'): ");
            string metin = Console.ReadLine() ?? "";

            if (metin.ToLower() == "exit") break;

            string sonuc = PythonAnaliziniCagir(metin);
            SonucuYorumla(sonuc);
        }
    }

    static string PythonAnaliziniCagir(string metin)
    {
       
        string scriptYolu = Path.Combine(PROJE_YOLU, "Model", "tahmin_et.py");
        string pythonYolu = Path.Combine(PROJE_YOLU, ".venv", "bin", "python");

        
        if (!File.Exists(pythonYolu))
        {
            pythonYolu = "python3"; 
        }

        ProcessStartInfo start = new ProcessStartInfo();
        start.FileName = pythonYolu;
        start.Arguments = $"\"{scriptYolu}\" \"{metin}\"";
        start.UseShellExecute = false;
        start.RedirectStandardOutput = true;
        start.RedirectStandardError = true;
        start.CreateNoWindow = true;

        try
        {
            using (Process process = Process.Start(start)!)
            {
                string output = process.StandardOutput.ReadToEnd();
                string error = process.StandardError.ReadToEnd();
                process.WaitForExit();

                if (!string.IsNullOrEmpty(error)) return "PYTHON_HATASI|" + error;
                return output.Trim();
            }
        }
        catch (Exception ex)
        {
            return "CSHARP_HATASI|" + ex.Message;
        }
    }

    static void SonucuYorumla(string hamSonuc)
    {
        string[] parcalar = hamSonuc.Split('|');
        if (parcalar.Length >= 2)
        {
            string durum = parcalar[0];
            string detay = hamSonuc.Substring(hamSonuc.IndexOf('|') + 1); 

            if (durum == "TEHLIKELI")
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine($"\n[!] DİKKAT: PHISHING TESPİT EDİLDİ");
                Console.WriteLine($"[!] Güven Skoru: {detay}");
            }
            else if (durum == "GUVENLI")
            {
                Console.ForegroundColor = ConsoleColor.Blue;
                Console.WriteLine($"\n[OK] Temiz.");
                Console.WriteLine($"[OK] Güven Skoru: {detay}");
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Yellow;
                Console.WriteLine("\n[Hata Detayı]: " + detay);
            }
            Console.ResetColor();
        }
        else
        {
            Console.WriteLine("\n[?] Yanıt Anlaşılamadı: " + hamSonuc);
        }
    }
}