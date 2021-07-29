# Modele Matematyczne

### #1 - Test jednorodności rozkładów Mersenne- Twister oraz rand()

#### C++

Test jednorodności - wynik - dla N = 10 000, i ilości powtórzeń = 100mln (dane połączone liniami dla uzyskania lepszego efektu graficznego) w Plot.png



###### Kod GnuPlot

```
plot 'random_rand().txt' using 1:2 title "Rand()" with linespoints,\
	 'random_rand().txt' using 1:2 title "Rand()" with linespoints  
```