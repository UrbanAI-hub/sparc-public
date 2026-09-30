### Overview
Does a dangerous-looking intersection actually cause more crashes? This project investigates whether formalizing the "visual safety impression" of traffic experts into a scalable computer vision model can improve crash predictions across Rotterdam's road network, compared to traditional traffic volume models.

### The Challenge
Evaluating intersection safety is traditionally a manual, time-consuming process reliant on expert site visits. While urban planners and engineers have a strong intuitive sense of what makes a crossing look dangerous, scaling this human judgment across an entire city is impossible. The challenge is determining whether artificial intelligence can learn this visual intuition from street-level imagery and, more importantly, whether that visual danger actually adds any new predictive value beyond standard traffic data.

### Objectives
* **Elicit and formalize** the visual safety judgments of expert traffic engineers using pairwise image comparisons.
* **Train a computer vision model** to scale these subjective expert scores across all intersections in Rotterdam.
* **Evaluate** whether this new visual safety metric improves the accuracy of conventional crash prediction models.

### Approach
The research team extracted Google Street View images for intersections across Rotterdam. They conducted an expert elicitation study where traffic engineers repeatedly chose the "more dangerous" looking intersection between pairs of images, creating a robust baseline of human judgment. A computer vision architecture was then trained to replicate and generalize these scores across the city network. Finally, these AI-generated visual risk scores were integrated into traditional statistical crash models—which rely on variables like traffic volume and speed—to see if the visual data added any incremental predictive power.

### Key Findings
* **AI can learn expert intuition:** The computer vision model successfully learned to replicate the visual safety scores of the human traffic engineers with moderate skill across the network.
* **Visuals mirror volume:** Despite capturing the "danger" accurately, the visual score did not improve actual crash predictions. This is because visual danger and traffic volume are deeply intertwined; an intersection that "looks dangerous" is typically just a very busy, wide road.
* **Traditional models hold strong:** The visual safety score largely re-encodes exposure and speed cues that traditional crash models already capture perfectly.

### Impact
For the Municipality of Rotterdam, this research provides strong validation that their current data-driven network screening approach (relying on traffic volume and speed) is already optimal, saving the city from investing heavily in redundant visual-assessment technologies for ranking purposes. However, the study unlocked a novel secondary use case: because the AI's visual score tracks traffic volume so closely, it can serve as a low-cost proxy to estimate traffic exposure in cities or newly built intersections where formal traffic registration data is missing.
