let arr = [5, 4, 3, 2, 1]

// iterate over array
// compare current value to previous value

function insertionSort(arr) {
	for (let i=0; i <= arr.length; i++) {
		for (let j = 0; j <= arr.length; j++) {
			if (arr[j] <= arr[j - 1]) {
				let lesser = arr[j]
				let greater = arr[j - 1]
				arr[j] = greater
				arr[j - 1] = lesser
				console.log('swap', arr[j], arr[j - 1], arr)
			} else {
				console.log('no swap')
			}
		}
	}
	console.log('final output', arr)
}

insertionSort(arr);