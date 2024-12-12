using System;
using System.Globalization;


/*
class Program
{
    static void Main()
    {
        double x1 = -10;     // Початок діапазону
        double x2 = -8;      // Кінець діапазону
        double deltaX = 0.4; // Крок

        for (double x = x1; x < x2; x += deltaX)
        {
            double y = Math.Sqrt(x + 9) / (x + 1) + 1 / (x + 2);
            Console.WriteLine($"x = {x}, y = {y}");
        }
    }
}
*/

/*
namespace Lab3_2 {
    class Program {

        static void Main()
        {

            // Випадок (а)

            double n = 7;
            double x = 0.2;
            double result_a = 0;


            for( int i = 1; i <= n; i++ )
            {
                result_a += (Math.Pow(x,3) / 3) + (Math.Pow(-1, i) * Math.Pow(x,3*i) / ((2*i -1)*(i+2)));
            }
            Console.WriteLine($"Завдання (а): при n = {n} та x = {x} результатом рахунку є: {result_a}");

            // Випадок (б)

            n = 7;
            x = 0.5;
            double result_b = 0;
            double epsilon = 0.001;
            double term;
            
            // Перший член ряду 
            result_b = Math.Pow(x, 3) / 3;
            for( int i = 1; i <= n ;i++ )
            {
                // Рахуємо до потрібного члену ряду
                term = (Math.Pow(-1, i) * Math.Pow(x,3*i) / ((2*i -1)*(i+2)));
                
                // Додаємо до результату
                result_b += term;

                // Перевірка точності члена ряду
                if (Math.Abs(term) < epsilon){
                    break;
                }
            }
                                           
            Console.WriteLine($"Завдання (б): при n = {n} та x = {x} та ε = {epsilon} результатом рахунку є: {result_b}");
            
            // Випадок (в)

            n = 7;
            x = 0.1;
            double x1 = 0.1;
            double x_end = 0.5;
            double h = 0.2;
            double result_c = 0;
            double term2 = 0;
            double epsilon2 = 0.00001;


            for(x = 0.1; x < 0.5; x += h)
            {
                for( int i = 1; i <= n; i++ )
            {
                result_c = Math.Pow(x, 3) / 3;
                // Рахуємо до потрібного члену ряду
                term2 = (Math.Pow(-1, i) * Math.Pow(x,3*i) / ((2*i -1)*(i+2)));
                
                // Додаємо до результату
                result_c += term2;

                // Перевірка точності члена ряду
                if (Math.Abs(term2) < epsilon2){
                    break;
                }

            }
                
            }
            Console.WriteLine($"Завдання (в): при x1 = {x1} до х2 = {x_end} з кроком h = {h} та ε = 0.00001 результатом рахунку є: {result_c}");
        }
    }
}*/


/*
class Program
{
    static void Main()
    {
        Console.Write("Введіть значення x (1 < x < 10): ");
        string input = Console.ReadLine();

        if (double.TryParse(input, CultureInfo.InvariantCulture, out double x))
        {
            // Перевірка діапазону
            if (x > 1 && x < 10)
            {
                // Обчислення меж
            int low = (int)(Math.Log(x));
            int high = (int)(Math.Exp(x));
            // Обчислення суми квадратів
            int sumOfSquares = 0;
            for (int i = low; i <= high; i++)
            {
                sumOfSquares += i * i;
            }
            // Виведення результату  
            
            Console.WriteLine($"Сума квадратів чисел у проміжку ({low}, {high}) дорівнює: {sumOfSquares}");
            }
            else
            {
                Console.WriteLine("Число має бути в межах (1, 10).");
            }
        }
        else
        {
            Console.WriteLine("Некоректне значення. Будь ласка, введіть число.");
        }

    
    }
}*/

