/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
using System;
class Lab3_Demo {
    static int factor(int n){
        int f = 1;
        int i = 1;
        while(i<=n){
            f = f*i;
            i++;
        }
        return (f);
    }
  static void Main() {
    double x = 0.5;
    double y = 0;
    double eps = 0.0001;
    double xn = 0;
    int i = 0;
    xn = Math.Pow(-1,i)*Math.Pow(x,2*i+1)/factor(2*i+1);
    while(Math.Abs(xn)>eps){
        y = y +xn;
        i++;
        xn = Math.Pow(-1,i)*Math.Pow(x,2*i+1)/factor(2*i+1);
    }
    Console.WriteLine("Factor(5)={0}",factor(5));
    Console.WriteLine("y={0}",y);
    double y1 = Math.Sin(x);
    Console.WriteLine("y1 ={0}",y1);
    
  }
}