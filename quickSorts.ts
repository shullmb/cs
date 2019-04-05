// TS quicksort - out of place 
function quickSort<T>(arr: T[]): T[] {
  if (arr.length <= 1) return arr
  else {
    let pivot: T = arr[Math.floor(arr.length / 2)]
    let mid: T[] = []
    let left: T[] = []
    let right: T[] = []

    arr.forEach(item => {
      if (item < pivot) left.push(item)
      if (item > pivot) right.push(item)
      if (item == pivot) mid.push(item)
    })

    return [...quickSort(left), ...mid, ...quickSort(right)]
  }
}

const test = [3, 4, 5, 1, 2, 3, 7, 10]
const strings = ['bat', 'cat', 'aat', 'gnat']