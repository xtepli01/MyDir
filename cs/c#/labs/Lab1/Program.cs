using System;

/*namespace Task1
{
    class Program
    {
        // Студент Tepliakov Oleksandr
        static void Main()
        {
            // Ввід і перевірка значення m
            Console.Write($"Введіть значення змінної m: ");
            double m = double.Parse(Console.ReadLine());

            Console.Write($"Введіть значення змінної n: ");
            double n = double.Parse(Console.ReadLine());

            Console.Write($"Введіть значення змінної alpha: ");
            double alpha = double.Parse(Console.ReadLine());



            // Виконання обчислень
            double exponentCube = Math.Pow(Math.E, 3);
            double cosAlpha = Math.Cos(alpha);
            double leftPart = (Math.Pow(m, 2) - Math.Pow(n, 2)) / (1 + cosAlpha);
            double rightPart = 4 * Math.Log(3.5) / 3;
            double sqrtPart = Math.Sqrt(rightPart - Math.Pow(cosAlpha, 2));

            double result = exponentCube + leftPart * sqrtPart;

            // Виведення результату
            Console.WriteLine($"Result of the expression is: {result}");
        }
    }
}*/
/*class Program{

    static void Main(){

        double k = 0.5;

        Console.Write("Введіть висоту першого трикутника: ");
        double h1 = double.Parse(Console.ReadLine());

        Console.Write("Введіть основу першого трикутника: ");
        double a1 = double.Parse(Console.ReadLine());

        double s1 = k * h1 * a1;
        Console.WriteLine($"Площа першого трикутника: {s1} ");


        Console.Write("Введіть висоту другого трикутника: ");
        double h2 = double.Parse(Console.ReadLine());

        Console.Write("Введіть основу другого трикутника: ");
        double a2 = double.Parse(Console.ReadLine());

        double s2 = k * h2 * a2;
        Console.WriteLine($"Площа другого трикутника: {s2} ");


        Console.Write("Введіть висоту третього трикутника: ");
        double h3 = double.Parse(Console.ReadLine());

        Console.Write("Введіть основу третього трикутника: ");
        double a3 = double.Parse(Console.ReadLine());
        
        double s3 = k * h3 * a3;
        Console.WriteLine($"Площа третього трикутника: {s3} ");

        double result = s1 - s2 + s3;
        Console.WriteLine($"Площа зафарбованої фігури: {result}");


    }
}*/

/*class Program
{
    static void Main()
    {
        // Введення значення a
        Console.Write("Введіть значення змінної a: ");
        double a = double.Parse(Console.ReadLine());

        // Обчислення значення котангенса
        double cotValue = Math.Exp(a) + 1;

        // Обчислення x через обернену функцію котангенса
        double x = Math.PI + Math.Atan(1 / cotValue); // Використовуємо арктангенс для оберненого котангенса

        // Перевірка інтервалу
        if (x > Math.PI && x < 2 * Math.PI)
        {
            Console.WriteLine($"Корінь рівняння у інтервалі (π, 2π) при a = {a} дорівнює x = {x}");
        }
        else
        {
            Console.WriteLine("Корінь не належить інтервалу (π, 2π).");
        }
    }
}*/





