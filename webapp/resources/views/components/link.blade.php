{{-- It's important that this file does NOT have a newline at the end. --}}
<a {{ $attributes->class([
    'inline font-medium underline',
    'text-(--color-accent-content) decoration-[color-mix(in_oklab,var(--color-accent-content),transparent_30%)]',
    'hover:decoration-current',
]) }}>{{ $slot }}</a>