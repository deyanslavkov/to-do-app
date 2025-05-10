import axios from 'axios';
import { Todo, CreateTodoDto, UpdateTodoDto } from '../types/Todo';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const axiosInstance = axios.create({
  baseURL: `${API_URL}/api`,
  headers: {
    'Content-Type': 'application/json',
  },
});

console.log("API URL:", API_URL);

export const todoService = {
  async getTodos(): Promise<Todo[]> {
    const response = await axiosInstance.get('/todos');
    return response.data;
  },

  async getTodoById(id: number): Promise<Todo> {
    const response = await axiosInstance.get(`/todos/${id}`);
    return response.data;
  },

  async createTodo(todo: CreateTodoDto): Promise<Todo> {
    const response = await axiosInstance.post('/todos', todo);
    return response.data;
  },

  async updateTodo(id: number, todo: UpdateTodoDto): Promise<Todo> {
    const response = await axiosInstance.patch(`/todos/${id}`, todo);
    return response.data;
  },

  async deleteTodo(id: number): Promise<void> {
    await axiosInstance.delete(`/todos/${id}`);
  },
};