import React from 'react';
import { CheckCircle } from 'lucide-react';

export const TodoHeader: React.FC = () => {
  return (
    <header className="mb-8">
      <div className="flex items-center justify-center mb-4">
        <CheckCircle className="text-blue-600 w-8 h-8 mr-2" />
        <h1 className="text-3xl font-bold text-gray-800">Todo App</h1>
      </div>
      <p className="text-center text-gray-600">
        Keep track of your tasks and stay organized
      </p>
    </header>
  );
};