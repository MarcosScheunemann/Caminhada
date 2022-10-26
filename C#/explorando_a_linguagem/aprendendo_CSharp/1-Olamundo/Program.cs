using System;

class Programa
{

    static void Main(string[] args)
    {
        Console.WriteLine("Olá, mundo");
        int idade;
        idade = 38;
        idade = idade - 2 * 9;
        double carteira = 53.696;
        char letra = 'a';
        string frase = "é assim que se declara uma string";

        Console.WriteLine(carteira + letra + frase);

        if (idade >=18 || letra == 'a' && idade == 38)
        {
            Console.WriteLine("Maiore");
        }
        else
        {
            Console.WriteLine("Menore");
        }


        int mes = 1;
        while (mes <= 12)
        {
            Console.WriteLine(mes);
            mes++;
        }

        Console.WriteLine(idade);
        Console.WriteLine("tecle enter para fechar...");
        Console.ReadLine();
    }
}

