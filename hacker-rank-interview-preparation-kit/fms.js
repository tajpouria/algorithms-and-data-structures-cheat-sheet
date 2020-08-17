function minimumSwaps(arr) {
    let newArr = [];
    let newArrVisited = [];
    for (let i = 0; i < arr.length; i++) {
        newArr[i] = [];
        newArr[i].value = arr[i];
        newArr[i].key = i;
        newArrVisited[i] = false;
    }

    // sort new array by value
    newArr.sort(function(a, b) {
        return a.value - b.value;
    });

    var swp = 0;
    for (let i = 0; i < arr.length; i++) {
        // check if already visited or swapped
        if (newArr[i].key == i || newArrVisited[i]) {
            continue;
        }

        var cycle = 0;
        var j = i;
        while (!newArrVisited[j]) {
            // mark as visited
            newArrVisited[j] = true;
            j = newArr[j].key; //assign next key
            cycle++;
        }
        if (cycle > 0) {
            swp += cycle > 1 ? cycle - 1 : cycle;
        }
    }
    return swp;
}

console.info(minimumSwaps([4, 3, 1, 2]));
