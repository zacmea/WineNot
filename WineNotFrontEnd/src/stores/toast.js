import {defineStore} from 'pinia'

export const useToastStore = defineStore({
    id: 'toast',

    state: () => ({
        ms: 0,
        message: '',
        classes: '',
        isVisible: false
    }),

    actions: {
        show({ms, message, classes}) {  // will make this popupup on screen, but not yet visible
            this.ms = parseInt(ms)
            this.message = message
            this.classes = classes
            this.isVisible = true

            setTimeout(() => {
                this.classes += ' -translate-y-28' //brings into view
            }, 10)

            setTimeout(() => {
                this.classes = this.classes.replace('-translate-y-28', '') //removes from view
            }, this.ms -500)
            
            setTimeout(() => {
                this.isVisible = false
            }, this.ms)
        }
    }
})