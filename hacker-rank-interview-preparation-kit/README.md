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
