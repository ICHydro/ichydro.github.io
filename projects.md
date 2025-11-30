---
layout: page
permalink: projects.html
style: header
---

<div class="section-title">
  <h3>Active Projects</h3>
  <div class="divider"></div>
</div>

<div class="project-gallery">
  {% for project in site.data.projects.active %}
  <div class="project-card" onclick="openProjectModal('{{ project.name | slugify }}')">
    <div class="project-logo">
      <img src="{{ '/assets/img/' | append: project.logo | relative_url }}" alt="{{ project.name }}">
    </div>
    <div class="project-info">
      <h4>{{ project.name }}</h4>
      <p class="period">{{ project.period }}</p>
      <p class="funding">{{ project.funding }}</p>
    </div>
  </div>
  {% endfor %}
</div>

<div class="section-title">
  <h3>Past Projects</h3>
  <div class="divider"></div>
</div>

<div class="project-gallery">
  {% for project in site.data.projects.past %}
  <div class="project-card" onclick="openProjectModal('{{ project.name | slugify }}')">
    <div class="project-logo">
      <img src="{{ '/assets/img/' | append: project.logo | relative_url }}" alt="{{ project.name }}">
    </div>
    <div class="project-info">
      <h4>{{ project.name }}</h4>
      <p class="period">{{ project.period }}</p>
      <p class="funding">{{ project.funding }}</p>
    </div>
  </div>
  {% endfor %}
</div>

<!-- Modals for project details -->
{% for project in site.data.projects.active %}
<div id="{{ project.name | slugify }}-modal" class="project-modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <div class="modal-project-logo">
      <img src="{{ '/assets/img/' | append: project.logo | relative_url }}" alt="{{ project.name }}">
    </div>
    <div class="modal-project-info">
      <h3>{{ project.name }}</h3>
      <p class="period"><strong>Period:</strong> {{ project.period }}</p>
      <p class="funding"><strong>Funding:</strong> {{ project.funding }}</p>
      <p class="role"><strong>Role:</strong> {{ project.role }}{% if project.lead %} (led by {{ project.lead }}){% endif %}</p>
      <p class="description">{{ project.description }}</p>
      {% if project.website %}
      <p class="website">
        <a href="{{ project.website }}" target="_blank" class="btn-link">
          Visit Project Website →
        </a>
      </p>
      {% endif %}
    </div>
  </div>
</div>
{% endfor %}

{% for project in site.data.projects.past %}
<div id="{{ project.name | slugify }}-modal" class="project-modal">
  <div class="modal-content">
    <span class="close">&times;</span>
    <div class="modal-project-logo">
      <img src="{{ '/assets/img/' | append: project.logo | relative_url }}" alt="{{ project.name }}">
    </div>
    <div class="modal-project-info">
      <h3>{{ project.name }}</h3>
      <p class="period"><strong>Period:</strong> {{ project.period }}</p>
      <p class="funding"><strong>Funding:</strong> {{ project.funding }}</p>
      <p class="role"><strong>Role:</strong> {{ project.role }}{% if project.lead %} (led by {{ project.lead }}){% endif %}</p>
      <p class="description">{{ project.description }}</p>
      {% if project.website %}
      <p class="website">
        <a href="{{ project.website }}" {% if project.website contains 'http' %}target="_blank"{% endif %} class="btn-link">
          Visit Project Website →
        </a>
      </p>
      {% endif %}
    </div>
  </div>
</div>
{% endfor %}

<script>
function openProjectModal(projectSlug) {
  const modal = document.getElementById(projectSlug + '-modal');
  if (modal) {
    modal.classList.add('active');
  }
}

// Close modal when clicking the X or outside the modal
document.addEventListener('DOMContentLoaded', function() {
  const modals = document.querySelectorAll('.project-modal');
  
  modals.forEach(modal => {
    // Close when clicking the X
    const closeBtn = modal.querySelector('.close');
    closeBtn.addEventListener('click', function() {
      modal.classList.remove('active');
    });
    
    // Close when clicking outside the modal content
    modal.addEventListener('click', function(e) {
      if (e.target === modal) {
        modal.classList.remove('active');
      }
    });
  });
  
  // Close with ESC key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
      modals.forEach(modal => {
        modal.classList.remove('active');
      });
    }
  });
});
</script>





