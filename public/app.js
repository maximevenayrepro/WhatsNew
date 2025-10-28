// =============================================================================
// State Management
// =============================================================================

// Hardcoded topics for initial implementation
const AVAILABLE_TOPICS = ['Tech', 'Crypto', 'Space'];

const state = {
    topics: AVAILABLE_TOPICS,
    selectedTopics: [],
    newsItems: [],
    isLoading: false,
    error: null
};

// =============================================================================
// DOM References
// =============================================================================

const DOM = {
    topicsList: null,
    refreshButton: null,
    newsList: null,
    loadingIndicator: null,
    errorMessage: null,
    modalRoot: null,
    modalBody: null,
    modalClose: null
};

// =============================================================================
// Initialization
// =============================================================================

function init() {
    // Cache DOM references
    DOM.topicsList = document.getElementById('topics-list');
    DOM.refreshButton = document.getElementById('refresh-button');
    DOM.newsList = document.getElementById('news-list');
    DOM.loadingIndicator = document.getElementById('loading-indicator');
    DOM.errorMessage = document.getElementById('error-message');
    DOM.modalRoot = document.getElementById('modal-root');
    DOM.modalBody = document.getElementById('modal-body');
    DOM.modalClose = document.getElementById('modal-close');

    // Attach event listeners
    attachEventListeners();

    // Render topics
    renderTopics();

    console.log('App initialized - topics rendered');
}

function attachEventListeners() {
    // Refresh button
    if (DOM.refreshButton) {
        DOM.refreshButton.addEventListener('click', handleRefreshClick);
    }

    // Modal close
    if (DOM.modalClose) {
        DOM.modalClose.addEventListener('click', closeModal);
    }

    // Modal backdrop click
    if (DOM.modalRoot) {
        DOM.modalRoot.addEventListener('click', (e) => {
            if (e.target === DOM.modalRoot || e.target.classList.contains('modal-backdrop')) {
                closeModal();
            }
        });
    }

    // Keyboard shortcuts
    document.addEventListener('keydown', handleKeyDown);
}

// =============================================================================
// Event Handlers
// =============================================================================

async function handleRefreshClick() {
    // Validate that at least one topic is selected
    if (state.selectedTopics.length === 0) {
        showError('Please select at least one topic');
        return;
    }

    // Clear previous error messages
    showError(null);

    // Update loading state
    state.isLoading = true;
    showLoading(true);
    
    // Disable refresh button during loading
    if (DOM.refreshButton) {
        DOM.refreshButton.disabled = true;
    }

    try {
        const results = await fetchNews(state.selectedTopics);
        state.newsItems = results;
        renderNews();
        console.log('Successfully fetched and rendered news for:', state.selectedTopics);
    } catch (error) {
        console.error('Error fetching news:', error);
        showError(error.message || 'Failed to fetch news. Please try again.');
    } finally {
        // Reset loading state
        state.isLoading = false;
        showLoading(false);
        
        // Re-enable refresh button
        if (DOM.refreshButton) {
            DOM.refreshButton.disabled = false;
        }
    }
}

function handleTopicChange(e) {
    const topicName = e.target.value;
    const isChecked = e.target.checked;

    if (isChecked) {
        // Add topic to selectedTopics if not already present
        if (!state.selectedTopics.includes(topicName)) {
            state.selectedTopics.push(topicName);
        }
    } else {
        // Remove topic from selectedTopics
        state.selectedTopics = state.selectedTopics.filter(t => t !== topicName);
    }

    console.log('Topics selection updated:', state.selectedTopics);
}

function handleKeyDown(e) {
    // Close modal on Escape
    if (e.key === 'Escape' && !DOM.modalRoot.classList.contains('hidden')) {
        closeModal();
    }
}

// =============================================================================
// Rendering Functions
// =============================================================================

function renderTopics() {
    if (!DOM.topicsList) {
        console.error('Topics list container not found');
        return;
    }

    // Clear existing content
    DOM.topicsList.innerHTML = '';

    // Create a checkbox for each topic
    state.topics.forEach(topic => {
        const checkboxContainer = document.createElement('div');
        checkboxContainer.className = 'topic-checkbox';

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.id = `topic-${topic.toLowerCase()}`;
        checkbox.name = 'topic';
        checkbox.value = topic;
        checkbox.addEventListener('change', handleTopicChange);

        const label = document.createElement('label');
        label.htmlFor = `topic-${topic.toLowerCase()}`;
        label.textContent = topic;

        checkboxContainer.appendChild(checkbox);
        checkboxContainer.appendChild(label);
        DOM.topicsList.appendChild(checkboxContainer);
    });

    console.log(`Rendered ${state.topics.length} topics`);
}

function renderNews() {
    if (!DOM.newsList) {
        console.error('News list container not found');
        return;
    }

    // Clear existing content
    DOM.newsList.innerHTML = '';

    // Check if we have results
    if (!state.newsItems || state.newsItems.length === 0) {
        DOM.newsList.innerHTML = '<p class="empty-state">No news found. Try selecting different topics.</p>';
        return;
    }

    // Render each topic section
    state.newsItems.forEach(topicData => {
        // Create topic section
        const topicSection = document.createElement('div');
        topicSection.className = 'topic-section';

        // Topic header
        const topicHeader = document.createElement('h3');
        topicHeader.className = 'topic-header';
        topicHeader.textContent = topicData.topic;
        topicSection.appendChild(topicHeader);

        // Check if topic has items
        if (!topicData.items || topicData.items.length === 0) {
            const emptyMsg = document.createElement('p');
            emptyMsg.className = 'topic-empty';
            emptyMsg.textContent = 'No news found for this topic';
            topicSection.appendChild(emptyMsg);
        } else {
            // Create list of news items
            const newsList = document.createElement('ul');
            newsList.className = 'news-items-list';

            topicData.items.forEach(item => {
                const listItem = document.createElement('li');
                listItem.className = 'news-item-simple';

                const link = document.createElement('a');
                link.href = item.url;
                link.target = '_blank';
                link.rel = 'noopener noreferrer';
                link.textContent = item.title;
                link.title = item.snippet; // Show snippet on hover

                listItem.appendChild(link);
                newsList.appendChild(listItem);
            });

            topicSection.appendChild(newsList);
        }

        DOM.newsList.appendChild(topicSection);
    });

    console.log(`Rendered ${state.newsItems.length} topic sections`);
}

function showLoading(show) {
    if (show) {
        DOM.loadingIndicator?.classList.remove('hidden');
    } else {
        DOM.loadingIndicator?.classList.add('hidden');
    }
}

function showError(message) {
    if (message) {
        DOM.errorMessage.textContent = message;
        DOM.errorMessage.classList.remove('hidden');
    } else {
        DOM.errorMessage.textContent = '';
        DOM.errorMessage.classList.add('hidden');
    }
}

// =============================================================================
// Modal Functions
// =============================================================================

function openModal(content) {
    if (DOM.modalBody && DOM.modalRoot) {
        DOM.modalBody.innerHTML = content;
        DOM.modalRoot.classList.remove('hidden');
        DOM.modalRoot.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
    }
}

function closeModal() {
    if (DOM.modalRoot) {
        DOM.modalRoot.classList.add('hidden');
        DOM.modalRoot.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
    }
}

// =============================================================================
// API Functions
// =============================================================================

async function fetchNews(topics) {
    const API_ENDPOINT = 'http://127.0.0.1:8000/api/get_news';
    const TIMEOUT_MS = 65000; // 65 seconds (backend has 60s timeout)

    // Create AbortController for timeout
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), TIMEOUT_MS);

    try {
        const response = await fetch(API_ENDPOINT, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ topics }),
            signal: controller.signal
        });

        clearTimeout(timeoutId);

        if (!response.ok) {
            // Handle HTTP errors
            const errorText = await response.text();
            throw new Error(`Server error (${response.status}): ${errorText}`);
        }

        const data = await response.json();
        return data;

    } catch (error) {
        clearTimeout(timeoutId);

        if (error.name === 'AbortError') {
            throw new Error('Request timeout - please try again');
        }
        
        if (error instanceof TypeError && error.message.includes('fetch')) {
            throw new Error('Network error - cannot reach server');
        }

        throw error;
    }
}

// =============================================================================
// Utility Functions
// =============================================================================

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { 
        year: 'numeric', 
        month: 'short', 
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

// =============================================================================
// App Entry Point
// =============================================================================

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}

