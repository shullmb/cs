import {LinkedList} from './LinkedList'

export class Storable<T> {
  constructor(
    protected store: LinkedList<T> = new LinkedList<T>()
  ) { }

  print(): void {
    this.store.print()
  }

  get length(): number {
    return this.store.length
  }
}

export class Stack<T> extends Storable<T> {
  push(data: T): void {
    this.store.add(data)
  }

  pop(): T {
    return this.store.delete(this.store.length - 1)
  }
}

export class Queue<T> extends Storable<T>{
  enqueue(data: T): void {
    this.store.add(data)
  }

  dequeue(): T {
    return this.store.delete(0)
  }
}