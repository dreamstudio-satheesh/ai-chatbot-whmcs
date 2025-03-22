import Alpine from 'alpinejs'

let root = {
    'x-data'() {
        return {
            trigger: undefined,
            menu: undefined,
            expanded: false,
            expand() {
                this.expanded = true
            },
            close(focus = true) {
                this.expanded = false
                focus
                    && !document.activeElement.isSameNode(this.trigger)
                    && setTimeout(() => this.trigger.focus())
            },
            toggle() {
                this.expanded ? this.close() : this.expand()
            },
        }
    },
    'x-id'() { return ['popover_trigger', 'popover_menu'] },
    '@keydown.escape.stop.prevent'() {
        this.$data.close()
    },
}

let trigger = {
    'x-init'() {
        this.$data.trigger = this.$el
    },
    ':id'() { return this.$id('popover_trigger') },
    ':aria-expanded'() { return this.$data.expanded },
    ':aria-controls'() { return this.$data.expanded && this.$id('popover_menu') },
    '@click'() { this.$data.toggle() },
}

let menu = {
    'x-init'() {
        this.$data.menu = this.$el
    },
    ':id'() { return this.$id('popover_menu') },
    'x-show'() { return this.$data.expanded },
    '@mousedown.window'($event) {
        this.$data.expanded
            && !this.$data.trigger.contains($event.target)
            && !this.$el.contains($event.target)
            && this.$data.close()
    }
}

export default () => ({
    init() {
        Alpine.bind(this.$el, root)
        Alpine.bind(this.$el.firstElementChild, trigger)
        Alpine.bind(this.$el.firstElementChild.nextElementSibling, menu)
    },
})
