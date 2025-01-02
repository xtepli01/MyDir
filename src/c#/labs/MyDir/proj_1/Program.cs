using System;

namespace DivisorCount
{
    class Program
    {
        static void Main()
        {
            int dividers = 0;
            int max_div = 0;
            int i = 1;

            while (i <= 100)
            {
                int counter = 0;
                int j = 1;

                while (j <= i)
                {
                    if (i % j == 0)
                    {
                        counter++;
                    }
                    j++;
                }

                if (counter > dividers)
                {
                    dividers = counter;
                    max_div = i;
                }

                i++;
            }

            Console.WriteLine($"Number in lenght 1 to 100 with max number of dividers: {max_div}");
            Console.WriteLine($"Number of divider: {dividers}");
        }
    }
}