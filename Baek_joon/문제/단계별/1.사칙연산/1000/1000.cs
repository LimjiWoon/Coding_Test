using System;
class Program
{
    static void Main()
    {
        //파이썬과 다르게 Console.ReadLine으로 글을 입력받는다
        string[] inputs = Console.ReadLine().Split();
        
        //byte.Parse()의 경우 안에 있는 내용을 변환한다.
        byte a = byte.Parse(inputs[0]);
        byte b = byte.Parse(inputs[1]);
        
        // 두 변수의 합을 출력
        Console.WriteLine(a + b);
    }
}   