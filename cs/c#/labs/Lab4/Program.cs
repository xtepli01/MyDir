using System;

/*
namespace Lab4_1{
    class Program{

        static void Main(){

            double [] x = new double [16];
            Random rand = new Random();

            for( int i = 0; i < x.Length; i++)
            {
                x[i] = rand.Next(0, 10);
            }

            double [] d = new double [16];
            double counter = 0;

            for(int i = 0; i < x.Length; i++)
                {
                    double k = x[i];
                    d[i] = (Math.Exp(k)+2*Math.Exp(-k))/Math.Sqrt(5+ Math.Sin(k));
                    if(d[i] < 0.1)
                    {
                        counter++;
                    }
                }

            Console.WriteLine("Массив1:" + string.Join(",", x));
            Console.WriteLine("Массив2:" + string.Join(",", d));
            Console.WriteLine($"Кількість елементів d > 0.1: {counter}");
        }
    }
}
*/

/*
class Program
{
    static void Main()
    {
        // Ініціалізація матриці 10x10 випадковими числами
        Random random = new Random();
        int[,] matrix = new int[10, 10];
        for (int i = 0; i < 10; i++)
        {
            for (int j = 0; j < 10; j++)
            {
                matrix[i, j] = random.Next(1, 101); // Випадкові числа від 1 до 100
                Console.Write(matrix[i, j] + "\t");
            }
            Console.WriteLine();
        }

        Console.WriteLine("\nРезультати:");

        int maxCount = 0;        // Максимальна кількість чисел, кратних 5
        int rowIndex = -1;       // Індекс рядка з максимальною кількістю

        // Перевірка кожного рядка
        for (int i = 0; i < 10; i++)
        {
            int count = 0;
            for (int j = 0; j < 10; j++)
            {
                if (matrix[i, j] % 5 == 0)
                {
                    count++;
                }
            }
            Console.WriteLine($"Рядок {i + 1}: {count} чисел, кратних 5");

            // Оновлення максимального значення і збереження індексу рядка
            if (count > maxCount)
            {
                maxCount = count;
                rowIndex = i;
            }
        }

        Console.WriteLine($"\nРядок із найбільшою кількістю чисел, кратних 5: {rowIndex + 1}");
    }
}
*/