import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 300000, // 2 minutes timeout for LLM generation
});

export const generateBackend = async (prompt) => {
  try {
    const response = await apiClient.post('/generate', {
      prompt: prompt
    });
    return response.data;
  } catch (error) {
    if (error.response) {
      throw new Error(error.response.data?.detail || error.response.data?.message || 'Generation failed');
    } else if (error.request) {
      throw new Error(
        error.response?.data?.detail ||
        error.message ||
        'AI generation failed. Please retry in a minute.'
      );
    } else {
      throw new Error(error.message || 'Request failed');
    }
  }
};

export default apiClient;