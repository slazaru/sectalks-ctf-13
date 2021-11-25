using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Challenge3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Booting up super secure application!");
            Console.WriteLine("Loading authentication module into memory!");
            byte[] flagbytes = Convert.FromBase64String("AFIHRgkNAUE7KW0zEA4BAVceGEkWXBBFHUIcCAVcbSslORdMGgpXHhhJHgMdU0lCKA0LUSU9");
            byte[] key1 = Encoding.ASCII.GetBytes("s7d2haj2@@@@dasdzsads2s7d2haj2@@@@dasdzsads2s7d2haj2@@@@dasdzsads2s7d2haj2@@@@dasdzsads2s7d2haj2@@@@dasdzsads2s7d2haj2@@@@dasdzsads2s7d2haj2@@@@dasdzsads2s7d2haj2@@@@dasdzsads2s7d2haj2@@@@dasdzsads2s7d2haj2@@@@dasdzsads2s7d2haj2@@@@dasdzsads2s7d2haj2@@@@dasdzsads2s7d2haj2@@@@dasdzsads2s7d2haj2@@@@dasdzsads2s7d2haj2@@@@dasdzsads2s7d2haj2@@@@dasdzsads2s7d2haj2@@@@dasdzsads2s7d2haj2@@@@dasdzsads2");
            byte[] result1 = new byte[54];
            for (int i = 0; i < result1.Length; i++)
            {
                result1[i] = 0;
            }

            Console.WriteLine("Loading plaintext administrator password into memory!");

            for (int i = 0; i < flagbytes.Length; i++)
            {
                result1[i] = (byte)(flagbytes[i] ^ key1[i]);
            }

            string result2 = System.Text.Encoding.UTF8.GetString(result1);

            Console.WriteLine("Enter password for Administrator:");
            string input1 = Console.ReadLine().Replace("\r\n", string.Empty);
            if (input1.Equals(result2))
            {
                Console.WriteLine("Successfully logged in!");
            } else
            {
                Console.WriteLine("AUTHENTICATION FAILED");
            }
            
        }
    }
}

