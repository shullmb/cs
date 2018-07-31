let arr = [84, 69, 51, 75, 83, 12, 2, 1, 11, 30, 42, 1]

// iterate over array
// compare current value to previous value

function insertionSort(arr) {
	counters = {swaps: 0, comparisons: 0}
	for (let i = 0; i <= arr.length; i++) {
		for (let j = 0; j <= arr.length; j++) {
			counters.comparisons += 1
			if (arr[j] < arr[j - 1]) {
				let lesser = arr[j]
				let greater = arr[j - 1]
				arr[j] = greater
				arr[j - 1] = lesser
				console.log('swap', arr[j], arr[j - 1], arr)
				counters.swaps += 1
			}
		}
	}
	console.log('final output', arr, 'num swaps: ', counters.swaps, 'num comps: ', counters.comparisons)
}

insertionSort(arr);