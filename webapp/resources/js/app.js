import 'instant.page'
import Alpine from 'alpinejs'
import ajax from '@imacrayon/alpine-ajax'
import Popover from './components/popover'

Alpine.plugin(ajax)
Alpine.data('popover', Popover)
Alpine.start()
