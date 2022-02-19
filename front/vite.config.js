import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  server: {
    host: '0.0.0.0',
    watch: {
      usePolling: true
    }
    // hmr: {
    //   port: 3010,
    //   clientPort: 3010,
    //   host: '0.0.0.0'
    // }
  }
})
