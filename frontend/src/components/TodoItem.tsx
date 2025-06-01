import React from 'react';
import { Check, Trash2 } from 'lucide-react';
import { Todo } from '../types/Todo';

interface TodoItemProps {
  todo: Todo;
  onToggle: () => void;
  onDelete: () => void;
}

export const TodoItem: React.FC<TodoItemProps> = ({ 
  todo, 
  onToggle, 
  onDelete 
}) => {
  return (
    <li className="px-4 py-3 hover:bg-gray-50">
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <button
            onClick={onToggle}
            className={`w-6 h-6 flex items-center justify-center rounded-full border ${
              todo.completed 
                ? 'bg-blue-500 border-blue-500 text-white' 
                : 'border-gray-300 bg-white'
            }`}
          >
            {todo.completed && <Check className="w-4 h-4" />}
          </button>
          <span 
            className={`${
              todo.completed 
                ? 'text-gray-400 line-through' 
                : 'text-gray-700'
            }`}
          >
            {todo.title}
          </span>
        </div>
        <button
          onClick={onDelete}
          className="text-gray-400 hover:text-red-500 focus:outline-none"
        >
          <Trash2 className="w-5 h-5" />
        </button>
      </div>
    </li>
  );
};