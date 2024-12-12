using System;

/*
namespace Lab2_1{

    class Program{

        static void Main(){

            Console.Write("Введіть значення х: ");
            double x = double.Parse(Console.ReadLine());
            double y;

            if ( 6.7 < x && x < 9.8)
            {

                y = (Math.Pow(x,2) + 2 * x + 7) / (Math.Pow(x, 2) + 2 * x + 3);
            }
            else if (x >= 9.8)
            {
                y = Math.Pow((Math.Pow(x, 2) + 1) / (Math.Pow(x, 3) + x - 1),2) + Math.Pow(x / (x + 1), 3);

            }
            else 
            {
                Console.WriteLine("Значення х не входить у область визначення функції");
                return;
            }

            Console.Write($"Значення y: {y}");
        }
    }
}*/

/*
namespace Lab2_2{

    class Program{

        static void Main(){

            Console.Write("Введіть координату х: ");
            double x = double.Parse(Console.ReadLine());
            Console.Write("Введіть координату у: ");
            double y = double.Parse(Console.ReadLine());

            if( y <= 0.5 * x + 1 && x >= -4 * y - 2)
            {
                Console.Write("Точка належить заштрихованій області");
            }
            else if ( y >= 0 && y <= 1 && x >= -2 && x <= 0)
            {
                Console.WriteLine("Точка належить заштрихованій області");
            }
            else if ( y >= 0.5 * x + 1 && x <= -4 * y - 2)
            {
                Console.WriteLine("Точка НЕ належить заштрихованій області");
            }
            else
            {
                Console.WriteLine("Точка НЕ належить заштрихованій області");
            }
        }
    }
}*/


/*namespace Lab2_3
{
class Program
 {
    static void Main()
    {
        // Параметри кола
        Console.WriteLine("Введіть параметри a,b,r кола");
        double a = double.Parse(Console.ReadLine());
        double b = double.Parse(Console.ReadLine());
        double r = double.Parse(Console.ReadLine());
cd
        // Точка для перевірки
        Console.WriteLine("Введіть координати точок кола");
        double x = double.Parse(Console.ReadLine());
        double y = double.Parse(Console.ReadLine());
    

        // Перевірка, чи належить точка колу
        if (Math.Pow(x - a, 2) + Math.Pow(y - b, 2) <= Math.Pow(r, 2))
        {
            Console.WriteLine("Точка належить колу.");
        }
        else
        {
            Console.WriteLine("Точка не належить колу.");
        }
    }
  }
}*/