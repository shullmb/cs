class Node
  attr_accessor :data, :next_node

  def initialize(data, next_node = nil)
    @data = data
    @next_node = next_node
  end
end

class LinkedList
  attr_accessor(:head, :length)
  def initialize
    @head = nil
    @length = 0
  end

  def increment_length
    @length += 1
  end
  
  def decrement_length
    @length -= 1
  end


  def add(data)
    node = Node.new(data)
    if @head == nil
      @head = node
      increment_length
    else
      current = @head
      while current.next_node != nil do
        current = current.next_node
      end
      current.next_node = node
      increment_length
    end
  end

  def delete_at_index(n)
    index = 0
    if @head == nil
      return false
    else
      current = @head
      while index < n do
        
      end
    end
  end

  def delete_where_data_equals(data)
    if @head == nil
      return false
    end
    current = @head
    if current.data == data
      temp_node = current.next_node
      current.next_node = nil
      @head = temp_node
      decrement_length
    else
      while current.next_node != nil do
        previous = current
        current = current.next_node
        if current.data == data
          temp_node = current.next_node
          previous.next_node = temp_node
          current.next_node = nil
          decrement_length
          return true
        end
      end
    end
    return false
  end

  def print_list
    if @head != nil
      current = @head
      print "[#{@head.data}"
      while current.next_node != nil do
        current = current.next_node
        print ", #{current.data}"
      end
      print "]\n"
    end
  end

end
