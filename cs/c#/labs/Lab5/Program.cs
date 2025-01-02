using System;/*
class Program
{
    static void Main()
    {
        Console.WriteLine("Введіть рядок:");
        string input = Console.ReadLine();

        // Розділення рядка на слова
        string[] words = input.Split(' ', StringSplitOptions.RemoveEmptyEntries);

        // Підрахунок
        int totalWords = words.Length;
        int matchingWords = 0;

        for (int i = 0; i < totalWords; i++)
        {
            string word = words[i];
            if (word.Length > 1 && char.ToLower(word[0]) == char.ToLower(word[word.Length - 1]))
            {
                matchingWords++;
            }
        }

        // Обчислення відсотка без тернарного оператора
        double percentage;
        if (totalWords == 0)
        {
            percentage = 0;
        }
        else
        {
            percentage = (matchingWords * 100.0) / totalWords;
        }

        // Виведення результатів
        Console.WriteLine($"Кількість слів: {totalWords}");
        Console.WriteLine($"Кількість слів, що починаються і закінчуються однаковим символом: {matchingWords}");
        Console.WriteLine($"Відсоток таких слів: {Math.Round(percentage, 2)}%");
    }
}*/

using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Введіть рядок із чисел, розділених пробілами:");
        string input = Console.ReadLine();

        // Розділення рядка на числа
        string[] numbers = input.Split(' ', StringSplitOptions.RemoveEmptyEntries);

        // Підрахунок парних чисел
        int cnt = 0;
        int i = 0;

        while (i < numbers.Length)
        {
            if (int.TryParse(numbers[i], out int n) && n % 2 == 0)
            {
                cnt++;
            }
            i++;
        }

        // Виведення результату
        Console.WriteLine($"Кількість парних чисел: {cnt}");
    }
}
