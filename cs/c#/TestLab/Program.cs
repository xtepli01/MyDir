using System;
/*class Program
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
}*/



class Program
{
    static void Main()
    {
        // Случай (a): n = 7, x = 0.2
        Console.WriteLine("Случай (a):");
        double x = 0.2;
        int n = 7;
        double result1 = CalculateSumFixedTerms(n, x);
        Console.WriteLine($"S (n = {n}, x = {x}) = {result1}");

        // Случай (б): x = 0.4, ε = 10^-4
        Console.WriteLine("\nСлучай (б):");
        x = 0.4;
        double epsilonB = 1e-4;
        double resultB = CalculateSumWithEpsilon(x, epsilonB);
        Console.WriteLine($"S (x = {x}, ε = {epsilonB}) = {resultB}");

        // Случай (в): x от 0.5 до 0.8 с шагом h = 0.1, ε = 10^-3
        Console.WriteLine("\nСлучай (в):");
        double startX = 0.5;
        double endX = 0.8;
        double step = 0.1;
        double epsilonV = 1e-3;

        for (x = startX; x <= endX; x += step)
        {
            double resultV = CalculateSumWithEpsilon(x, epsilonV);
            Console.WriteLine($"S (x = {x:F1}, ε = {epsilonV}) = {resultV}");
        }
    }

    // Метод для вычисления суммы с фиксированным количеством членов (для случая a)
    static double CalculateSumFixedTerms(int n, double x)
    {
        double result1 = Math.Pow(x, 3) / 3.0; // Перший член: x^3 / 3
        for (int k = 1; k <= n; k++) // Цикл від 1 до n, де n — спільна кількість членів
        {
            double local = Math.Pow(-1, k) * Math.Pow(x, 3 * k) / ((2.0 * k - 1) * (k + 2));
            result1 = result1 + local; // Результат
        }
        return result1; // Повертаємо результат функції
    }

    // Метод для вычисления суммы с точностью ε (для случаев б и в)
    static double CalculateSumWithEpsilon(double x, double epsilon)
    {
        double sum = x * x * x / 3.0; // Первый член суммы: x^3 / 3
        int k = 1;
        while (true)
        {
            double term = Math.Pow(-1, k) * Math.Pow(x, 3 * k) / ((2.0 * k - 1) * (k + 2));
            if (Math.Abs(term) < epsilon) break; // Прерываем цикл, если текущий член меньше ε
            sum += term;
            k++;
        }
        return sum;
    }
}



