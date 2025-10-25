describe('Login Flow', () => {
    beforeEach(() => {
        cy.clearLocalStorage();
        cy.visit('/login');
    });

    it('should display login page', () => {
        cy.get('h1').should('have.text', 'Login');
        cy.get('input[type="email"]').should('be.visible');
        cy.get('input[type="password"]').should('be.visible');
        cy.get('button[type="submit"]').should('be.visible');
    });

    it('should show error with invalid credentials', () => {
        cy.get('input[type="email"]').clear().type('wrong@email.com');
        cy.get('input[type="password"]').clear().type('wrongpassword');
        cy.get('button[type="submit"]').click();

        // Wait for error to appear
        cy.get('.bg-red-100', { timeout: 10000 }).should('be.visible');

        // Should still be on login page
        cy.url().should('include', '/login');
    });

    it('should successfully login with valid credentials', () => {
        cy.get('input[type="email"]').clear().type('test@t.ca');
        cy.get('input[type="password"]').clear().type('123456Pw');
        cy.get('button[type="submit"]').click();

        // Should redirect to home page (port 3000)
        cy.url().should('eq', 'http://localhost:3000/');

        // Token should be stored
        cy.window().then((win) => {
            const token = win.localStorage.getItem('token');
            expect(token).to.exist;
        });
    });
});