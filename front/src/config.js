console.log(import.meta.env.DEV, import.meta.env.VITE_API_ROOT, window.location.origin)
export const API_ROOT = import.meta.env.DEV ? import.meta.env.VITE_API_ROOT : window.location.origin