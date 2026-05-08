import axios from 'axios';

const API_BASE_URL = 'https://ai-software-compiler1.onrender.com';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 120000, // 2 minutes timeout for LLM generation
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
      throw new Error('No response from server. Make sure the backend is running on port 8000');
    } else {
      throw new Error(error.message || 'Request failed');
    }
  }
};

export default apiClient;