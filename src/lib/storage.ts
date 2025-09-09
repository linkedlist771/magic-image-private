import { ApiConfig, GeneratedImage, CustomModel } from "@/types"

// 硬编码的固定API URL
const FIXED_API_URL = "https://newapi.585dg.com"

const STORAGE_KEYS = {
  API_CONFIG: 'ai-drawing-api-config',
  HISTORY: 'ai-drawing-history',
  CUSTOM_MODELS: 'ai-drawing-custom-models',
  LAST_SELECTED_MODEL: 'ai-drawing-last-selected-model'
}

export const storage = {
  // API 配置相关操作
  getApiConfig: (): ApiConfig | null => {
    if (typeof window === 'undefined') return null
    const data = localStorage.getItem(STORAGE_KEYS.API_CONFIG)
    const config = data ? JSON.parse(data) : null
    // 强制使用固定的API URL，无论存储中是什么
    if (config) {
      config.baseUrl = FIXED_API_URL
    }
    return config
  },

  setApiConfig: (key: string, baseUrl: string): void => {
    if (typeof window === 'undefined') return
    const apiConfig: ApiConfig = {
      key,
      baseUrl: FIXED_API_URL, // 强制使用固定的API URL
      createdAt: new Date().toISOString()
    }
    localStorage.setItem(STORAGE_KEYS.API_CONFIG, JSON.stringify(apiConfig))
  },

  removeApiConfig: (): void => {
    if (typeof window === 'undefined') return
    localStorage.removeItem(STORAGE_KEYS.API_CONFIG)
  },

  // 历史记录相关操作
  getHistory: (): GeneratedImage[] => {
    if (typeof window === 'undefined') return []
    const data = localStorage.getItem(STORAGE_KEYS.HISTORY)
    return data ? JSON.parse(data) : []
  },

  addToHistory: (image: GeneratedImage): void => {
    if (typeof window === 'undefined') return
    const history = storage.getHistory()
    history.unshift(image)
    localStorage.setItem(STORAGE_KEYS.HISTORY, JSON.stringify(history))
  },

  clearHistory: (): void => {
    if (typeof window === 'undefined') return
    localStorage.removeItem(STORAGE_KEYS.HISTORY)
  },

  removeFromHistory: (id: string): void => {
    if (typeof window === 'undefined') return
    const history = storage.getHistory()
    const filtered = history.filter(img => img.id !== id)
    localStorage.setItem(STORAGE_KEYS.HISTORY, JSON.stringify(filtered))
  },

  // 自定义模型相关操作
  getCustomModels: (): CustomModel[] => {
    if (typeof window === 'undefined') return []
    const data = localStorage.getItem(STORAGE_KEYS.CUSTOM_MODELS)
    return data ? JSON.parse(data) : []
  },

  addCustomModel: (model: CustomModel): void => {
    if (typeof window === 'undefined') return
    const models = storage.getCustomModels()
    models.push(model)
    localStorage.setItem(STORAGE_KEYS.CUSTOM_MODELS, JSON.stringify(models))
  },

  removeCustomModel: (id: string): void => {
    if (typeof window === 'undefined') return
    const models = storage.getCustomModels()
    const filtered = models.filter(model => model.id !== id)
    localStorage.setItem(STORAGE_KEYS.CUSTOM_MODELS, JSON.stringify(filtered))
  },

  updateCustomModel: (id: string, updated: Partial<CustomModel>): void => {
    if (typeof window === 'undefined') return
    const models = storage.getCustomModels()
    const index = models.findIndex(model => model.id === id)
    if (index !== -1) {
      models[index] = { ...models[index], ...updated }
      localStorage.setItem(STORAGE_KEYS.CUSTOM_MODELS, JSON.stringify(models))
    }
  },

  // 最后选择的模型相关操作
  getLastSelectedModel: (): string | null => {
    if (typeof window === 'undefined') return null
    return localStorage.getItem(STORAGE_KEYS.LAST_SELECTED_MODEL)
  },

  setLastSelectedModel: (model: string): void => {
    if (typeof window === 'undefined') return
    localStorage.setItem(STORAGE_KEYS.LAST_SELECTED_MODEL, model)
  }
} 