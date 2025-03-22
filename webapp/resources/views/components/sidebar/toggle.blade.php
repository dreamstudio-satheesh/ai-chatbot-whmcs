<x-button
    type="button"
    x-init=""
    x-on:click="document.body.hasAttribute('data-show-stashed-sidebar') ? document.body.removeAttribute('data-show-stashed-sidebar') : document.body.setAttribute('data-show-stashed-sidebar', '')"
    aria-label="{{ __('Toggle sidebar') }}"
    {{ $attributes->class(['shrink-0']) }}
>{{ $slot }}</x-button>
