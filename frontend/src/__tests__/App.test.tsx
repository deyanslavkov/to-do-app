import { render, screen } from '@testing-library/react';
import App from '../App';
import { todoService } from '../services/todoService';

// Mock the todoService
jest.mock('../services/todoService');

describe('App Component', () => {
  beforeEach(() => {
    // Reset mocks
    jest.resetAllMocks();
    
    // Mock the getTodos method
    (todoService.getTodos as jest.Mock).mockResolvedValue([
      { id: 1, title: 'Test todo', completed: false }
    ]);
  });

  it('renders the header', async () => {
    render(<App />);
    expect(screen.getByText('Todo App')).toBeInTheDocument();
  });

  it('shows loading state initially', () => {
    render(<App />);
    expect(screen.getByText('Loading tasks...')).toBeInTheDocument();
  });

  it('displays todos after loading', async () => {
    render(<App />);
    
    // Wait for the todos to load
    const todoItem = await screen.findByText('Test todo');
    expect(todoItem).toBeInTheDocument();
  });
});