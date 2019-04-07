type ListNode<T> = LLNode<T> | null;

export class LLNode<T> {
  constructor(private _data: T, public next: ListNode<T> = null) {
  }

  get data(): T {
    return this._data
  }

  set data(payload) {
    this._data = payload
  }
}

export class LinkedList<T> {
  constructor(
    private head: ListNode<T> = null,
    private tail: ListNode<T> = null,
    public length: number = 0) {

  }

  add(data): void {
    let node = new LLNode<T>(data)
    if (this.head === null) {
      this.head = node
    } else {
      // let current = this.head
      // while (current.next) {
      //   current = current.next
      // }
      // [current.next, this.tail] = [node, node]
      let current = this.tail
      current.next = node
    }
    this.tail = node
    this.length++
  }

  delete<T>(deleteIndex: number): T {
    if (this.length > 0 && deleteIndex <= this.length - 1) {
      let result
      if (deleteIndex === 0) {
        result = this.head.data
        this.length--
        if (this.head.next) {
          this.head = this.head.next
          return result
        } else {
          console.log('firing')
          this.head = null
          this.tail = null
          return result
        }
      } else {
        let currentIndex = 0
        let current = this.head
        let previous
        while (currentIndex < deleteIndex) {
          previous = current
          current = current.next
          currentIndex++
        }
        result = current.data
        if (deleteIndex === this.length - 1) {
          this.tail = previous
        }
        previous.next = current.next
        this.length--
        return result
      }
    } else {
      console.log('popping')
      return null
    }
  }

  pop<T>(): T {
    return this.delete(this.length - 1)
  }

  shift<T>(): T {
    return this.delete(0)
  }

  print(): void {
    if (this.head !== null) {
      let arr: any[] = []
      let current = this.head
      while (current.next !== null) {
        arr.push(current.data)
        current = current.next
      }
      arr.push(current.data)
      console.log(arr)
    } else {
      console.log('empty list')
    }
  }
}