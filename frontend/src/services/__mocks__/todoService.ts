// frontend/src/services/__mocks__/todoService.ts

// We use jest.fn() to create mock functions that Jest can track.
// We make them return empty promises or simple data, which is usually
// enough for basic component rendering tests.

export const todoService = {
  getTodos: jest.fn().mockResolvedValue([]),
  addTodo: jest.fn().mockResolvedValue({ id: 'mock-id-1', title: 'Mocked Todo', completed: false }),
  updateTodo: jest.fn().mockResolvedValue({ id: 'mock-id-1', title: 'Mocked Todo', completed: true }),
  deleteTodo: jest.fn().mockResolvedValue(undefined),
};