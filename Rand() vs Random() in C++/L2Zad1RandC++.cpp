// L2Zad1RandC++.cpp 
// Autor - Paweł Leszczyński
// Na podstawie wykładu  "Liczby Pseudolosowe" autorstwa dr-a M.Matyki

#include <iostream>
#include <random>
#include <fstream>

std::mt19937 mt(time(NULL));
std::uniform_real_distribution<double> random(0, 1.0);

double wynik_random()
{
    return random(mt);
}



int main()
{
    //Pomysł "kubełkowy" z wykładu: losujemy liczby z zakresu 0-1, wkładamy je do "kubełków" 0-100. Z tego rysujemy histogram.
    const int N = 10000;
    const unsigned long int repeat = 100000000;
    int tab_rand[N + 1] = { 0 };
    int tab_random[N + 1] = { 0 };

    //Funkcja rand():
    // 

    std::cout << "Funkcja rand():\n";
    srand(time(NULL));
    for(int i = 0; i < repeat; i++)
    { 
        double temp_rand = rand() / float (RAND_MAX + 1);
        int elem_rand = int(floor(temp_rand * N));
        tab_rand[elem_rand]++;
    }

    std::ofstream file_one;
    file_one.open("random_rand().txt");

    for (int j = 0; j < N; j++)
    {
        file_one << j << " " << tab_rand[j] << "\n";
    }
    file_one.close();

    std::cout << "--------------\n";
    //Funkcja random() - korzystająca z algorytmu Mersenne Twister:

    std::cout << "Funkcja random():\n";
    for (int i = 0; i < repeat; i++)
    {
        double temp_random = random(mt);
        int elem_random = int(floor(temp_random * N));
        tab_random[elem_random]++;
    }

    std::ofstream file_two;
    file_two.open("random_random().txt");

    for (int j = 0; j < N; j++)
    {
        //std::cout << "i:" << j << " | wynik random(): " << tab_random[j] << "\n";
        file_two << j << " " << tab_random[j] << "\n";
    }
    file_two.close();

    return 0;
}

