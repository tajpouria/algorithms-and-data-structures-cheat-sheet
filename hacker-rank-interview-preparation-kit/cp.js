function minimumSwaps(arr) {
    const col = [],
        visited = [];

    for (let i = 0; i < arr.length; i++) {
        col[i] = { key: i, val: arr[i] };
        visited[i] = false;
    }

    col.sort((a, b) => a.val - b.val);

    console.log(col);

    let swp = 0;
    for (let i = 0; i < arr.length; i++) {
        if (col[i].key === i || visited[i]) {
            continue;
        }

        let cycle = 0,
            k = i;

        while (!visited[k]) {
            visited[k] = true;
            k = col[k].key;
            cycle++;
        }

        if (cycle > 0) {
            swp += cycle > 1 ? cycle - 1 : cycle;
        }
    }

    return swp;
}

console.info(minimumSwaps([4, 3, 1, 2]));
