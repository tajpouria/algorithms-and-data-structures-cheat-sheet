## [The HackerRank Interview Preparation Kit](https://www.hackerrank.com/interview/interview-preparation-kit)

### [Arrays: Left Rotation](https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays)

-   In order to do the array **right** rotation:

example: Rotate [1, 2, 3, 4, 5, 6], 4 element to the right _(result: [3, 4, 5, 6, 1, 2])_:

1. Reverse whole array: [`6, 5, 4, 3, 2, 1`]

2. Reverse first `k` element _(k=4)_: [`3, 4, 5, 6,` 2, 1]

3. Reverse `k` to end: [3, 4, 5, 6, `1, 2`]

In order to do the array **left** rotation:

example: Rotate [1, 2, 3, 4, 5], 4 element to the left _(result: [5, 1, 2, 3, 4])_:

1. Reverse whole array: [`5, 4, 3, 2, 1`]

2. Reverse last `k` element _(k=4)_: [5, `1, 2, 3, 4`]

3. Reverse from start to last `k` to end: [`4, 3`, 4, 3, 2, 1]

-   Reverse elements between to indexes:

```js
function reverse(arr, start, end) {
    while (star < end) {
        const tmp = arr[start];
        arr[start] = arr[end];
        arr[end] = emp;

        start++;
        end++;
    }

    return arr;
}
```

### [Minimum Swaps 2](https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen)

-   In order to find minimum number of swap needed to make an array sorted [Video](https://www.youtube.com/watch?v=f7IIW0HVUcQ)):

```js
function minimumSwap(arr) {
    const dic = [],
        visited = [];

    for (let i = 0; i < arr.length; i++) {
        dic[i] = { key: i, val: arr[i] };
        visited[i] = false;
    }
    dic.sort((a, b) => a.val - b.val);

    /*
      dic: [
       {key: 0, val: 1}
       {key: 2, val: 2}
       {key: 1, val: 3}
       {key: 3, val: 4}
      ]
    */

    let swp = 0;
    for (let i = 0; i < arr.length; i++) {
        if (dic[i].key === i || visited[i]) continue;

        let cycle = 0,
            k = i;
        while (!visited[i]) {
            visited[i] = true;
            k = dic[i].key;
            cycle++;
        }

        if (cycle > 0) {
            swp += cycle > 1 ? cycle - 1 : cycle;
        }
    }

    return swp;
}

minimumSwap([1, 3, 2, 4]);
```
