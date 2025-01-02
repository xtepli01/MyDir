using System;

/*class Target1
{
    // Approach of student Tepliakov Oleksandr to solve 20's variant
    // Correct input data is: "134" 
    static void Main(string[] args)
    {
        // Buffer
        string input;

        // Prompt user to enter a decimal integer
        Console.Write("Write a decimal: ");
        input = Console.ReadLine();

        // Validate input and parse to an integer
        if (int.TryParse(input, out int decimalNumber))
        {
            // Convert to different bases
            string binaryNumber = Convert.ToString(decimalNumber, 2);
            string hexNumber = Convert.ToString(decimalNumber, 16);
            string octalNumber = Convert.ToString(decimalNumber, 8);

            // Display the results
            Console.WriteLine($"To binary: {binaryNumber}");
            Console.WriteLine($"To hex: 0x{hexNumber}");
            Console.WriteLine($"To octal: 0x{octalNumber}");
        }
        else
        {
            Console.WriteLine("Invalid input. Please enter a valid integer.");
        }
    }
}*/


/*class Target2
{    
    // Approach of student Tepliakov Oleksandr to solve 20's variant
    // Correct input data is: "11110101" 

    // Function to check if the input is a binary number
    static bool IsBinary(string input)
    {
        // Check that string is not empty or null
        if (string.IsNullOrEmpty(input)){
            return false;
        }
        foreach (char c in input){
            if (c != '0' && c != '1') // Mask for characters 0 and 1 (control input only digits 0 and 1)
            {
                return false; 
            }
        }
        return true; // All characters are valid binary digits
    }
    static void Main()
    {
        string input;

        // Prompt user to write a binary number 
        Console.Write("Write a binary number: ");
        input = Console.ReadLine();

        // Validate input to ensure that is a binary number
        if (IsBinary(input))
        {
            // Convert binary to decimal
            int decimalNumber = Convert.ToInt32(input, 2);

            // Convert to hexadecimal base
            string hexNumber = Convert.ToString(decimalNumber, 16).ToUpper();

            // Display the results
            Console.WriteLine($"To decimal: {decimalNumber}");
            Console.WriteLine($"To hex: {hexNumber}");
        }
        else
        {
            Console.WriteLine("Invalid input. Please enter a valid binary number (only 0s and 1s).");
        }
    }
}*/


/*class Target3
{
    // Approach of student Tepliakov Oleksandr to solve 20's variant
    // Correct input data is: "9C" 

    // Function to check if the input is a hexadecimal number
    static bool IsHexadecimal(string input)
    {
        // Check that string is not empty or null
        if (string.IsNullOrEmpty(input)){
            return false;
        }
        
        // Check if character is bteween 0-9 or A-F/a-f
        foreach (char c in input){
            if (!((c >= '0' && c <= '9') || (c >= 'A' && c <= 'F') || (c >= 'a' && c <= 'f')))
            {
                return false;
            }
        }
        return true; // All characters are valid hexadecimal digits
    }
    static void Main()
    {
        // Buffer
        string input;

        // Prompt user to enter a hexadecimal number
        Console.Write("Write a hexadecimal number: ");
        input = Console.ReadLine();

        // Validate input to ensure it is a hexadecimal number
        if (IsHexadecimal(input))
        {
            // Convert hexadecimal to decimal
            int decimalNumber = Convert.ToInt32(input, 16);

            // Convert decimal binary base
            string binaryNumber = Convert.ToString(decimalNumber, 2);

            // Display the results
            Console.WriteLine($"To decimal: {decimalNumber}");
            Console.WriteLine($"To binary: {binaryNumber}");
        }
        else
        {
            // Output if input is incorrected
            Console.WriteLine("Invalid input. Please enter a valid hexadecimal number.");
        }
    }

}*/



