#include <vector>
#include<iostream>
#include<random>
#include <fstream>
using namespace std;

int main()
{
    double rand_x, rand_y, origin_dist, pi;
    int circle_points = 0, square_points = 0;
    std::vector< double > arr;
    
    srand(time(NULL));
    std::ofstream file;
    file.open("rand().txt");
    
    for (int i = 1; i < 100; i++) {
        for (int j = 0; j < (i * i); j++) {

            rand_x = double(rand() % (i + 1)) / i;
            rand_y = double(rand() % (i + 1)) / i;

            origin_dist = rand_x * rand_x + rand_y * rand_y;

            if (origin_dist <= 1)
                circle_points++;

            square_points++;       
        }
        pi = double(4 * circle_points) / square_points;
        file << pi<<",";
    }
    file.close();
    return 0;
}