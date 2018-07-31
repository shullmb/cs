let arr = [2,5,3,6,4,2,6,3,8,5]

// i think i'm missing some things
function mergeSort(array) {
    let arr = array
    if (arr.length <= 1) {
        console.log('base', arr)
        return arr
    } else {
        let middle = Math.ceil(arr.length / 2)
        console.log('recurse', arr)
        topHalf = arr.slice(middle,arr.length);
        bottomHalf = arr.slice(0,middle);
        console.log(topHalf, bottomHalf)
        return mergeSort()
    }
}
    
mergeSort(arr);
