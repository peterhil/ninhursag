<script lang="ts">
	import '$style/app.scss'

	import type { Snippet } from 'svelte';

	import Alerts from '$component/Alerts.svelte'

	interface Props {
		children?: Snippet
	}

	let { children }: Props = $props()
</script>

<svelte:head>
	<title>Ninhursag</title>
</svelte:head>

<Alerts />
{@render children?.()}
