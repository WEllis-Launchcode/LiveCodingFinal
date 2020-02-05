using System;

namespace LiveCodingFinal
{
    class Program
    {
        static void Main(string[] args)
        {
            string weather;
            int tempature;
            Console.WriteLine("Enter the weather: ");
            weather = Console.ReadLine();
            Console.WriteLine("Enter the temature: ");
            tempature = Convert.ToInt32(Console.ReadLine());
            if ((weather == "clear") && (tempature == 50))
            {
                double total = (250 + (250 * 0.10) + (250 * 0)) *3;
                Console.WriteLine(total);
            }

            if ((weather == "clear") && (tempature >= 50 && tempature <= 59))
            {
                double total = (250 + (250 * 0.10) + (250 * 0)) * 3;
                Console.WriteLine(total);
            }
            if ((weather == "full moon") && (tempature >= 40 && tempature <= 49))
            {
                double total = (250 + (250 * 0.25) - (250 * 0.05)) * 3;
                Console.WriteLine(total);
            }
            if ((weather == "raining") && (tempature >= 70 && tempature <= 79))
            {
                double total = (250 - (250 * 0.25) + (250 * 0.20)) * 3;
                Console.WriteLine(total);
            }
        }
    }
}
