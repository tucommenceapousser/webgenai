import { gsap } from "gsap";

export function applyGlitchEffect() {
    gsap.to("body", {
        duration: 0.1,
        x: () => (Math.random() - 0.5) * 10,
        y: () => (Math.random() - 0.5) * 10,
        repeat: 3,
        yoyo: true
    });
}
