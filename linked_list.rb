class Node
  attr_accessor(:data, :next_node)
  def initialize(data)
    @data = data
    @next_node = nil
  end
end

class LinkedList
  attr_accessor(:head)
  def initialize
    @head = nil
  end

  def add(data)
    node = Node.new(data)
    if @head == nil
      @head = node
    else
      current = @head
      while current != nil
        current = current.next_node
      end
      current.next_node = node
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
    else
      while current.next_node != nil
        previous = current
        current = current.next_node
        if current.data == data
          temp_node = current.next_node
          previous.next_node = temp_node
          current.next_node = nil
          return true
        end
      end
    end
    return false
  end

  def print_list
    if @head != nil
      current = @head
      puts @head.data
      while current.next_node != nil
        current = current.next_node
        puts current.data
      end
    end
  end

end

list = LinkedList.new

list.add("one")
list.print_list();