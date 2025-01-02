using System;

namespace Task1Calculation
{
    class Program
    {
        static void Main(string[] args)
        {
            // Define the values for m, n, and alpha
            double m = 9; // Example value for m
            double n = 2; // Example value for n
            double alpha = 1.45;

            // Calculate the expression
            double result = CalculateExpression(m, n, alpha);

            // Output the result
            Console.WriteLine("Result of the expression is: " + result);
        }

        static double CalculateExpression(double m, double n, double alpha)
        {
            // Calculate each part of the expression
            double eCubed = Math.Pow(Math.E, 3);
            double cosAlpha = Math.Cos(alpha);
            double part1 = (Math.Pow(m, 2) - Math.Pow(n, 2)) / (1 + cosAlpha);
            double lnPart = 4 * Math.Log(3.5) / 3;
            double sqrtPart = Math.Sqrt(lnPart - Math.Pow(cosAlpha, 2));

            // Combine all parts
            return eCubed + part1 * sqrtPart;
        }
    }
}
