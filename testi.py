int SComparison = 0;
int SSwaps = 0;

for (int i = 0; i < SorBag.length - 1; i++) {
        min = i;

        for (int j = i + 1; j < SorBag.length; j++) {
            SComparison++;

            if (SorBag[j] < SorBag[min]) {
                min = j;

            }
        }

        SSwaps++;
        temp2 = SorBag[i];
        SorBag[i] = SorBag[min];
        SorBag[min] = temp2;
    }