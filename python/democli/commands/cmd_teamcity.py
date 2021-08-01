import click
from democli.cli import pass_context
from democli.utils.click_util import common_options
from democli.utils.log_util import create_logger
from pyteamcity import TeamCity

logger = create_logger(__name__)

# common options for sub commands
_common_options = [
    click.option(
        '-s', '--server', required=True, help='The teamcity server address'
    ),
    click.option(
        '-t', '--port', type=int, default=80, help='The teamcity server port'
    ),
    click.option(
        '-u', '--auth_username', required=True, help='The username of the user for teamcity authentication'
    ),
    click.option(
        '-p', '--auth_password', required=True, help='The password of the user for teamcity authentication'
    )
]


@click.group('teamcity', short_help='Root command to interact with teamcity apis')
@pass_context
def cli(ctx):
    """Root command to interact with teamcity apis"""
    pass


@cli.command('get_projects', short_help='Get projects')
@common_options(_common_options)
@pass_context
def get_projects(ctx, server, port, auth_username, auth_password):
    """Get projects"""
    tc = TeamCity(auth_username, auth_password, server, port)
    tc.get_projects()


@cli.command('get_project_by_project_id', short_help='Get project by projectId')
@common_options(_common_options)
@click.option('--project_id', required=True, help='The project id')
@pass_context
def get_project_by_project_id(ctx, server, port, auth_username, auth_password, project_id):
    """Get project by projectId"""
    tc = TeamCity(auth_username, auth_password, server, port)
    tc.get_project_by_project_id(project_id)


@cli.command('get_all_users', short_help='Get all users')
@common_options(_common_options)
@pass_context
def get_all_users(ctx, server, port, auth_username, auth_password):
    """Get all users"""
    tc = TeamCity(auth_username, auth_password, server, port)
    tc.get_all_users()


@cli.command('get_user_by_username', short_help='Get user by username')
@common_options(_common_options)
@click.option('--username', required=True, help='The username')
@pass_context
def get_user_by_username(ctx, server, port, auth_username, auth_password, username):
    """Get user by username"""
    tc = TeamCity(auth_username, auth_password, server, port)
    tc.get_user_by_username(username)


@cli.command('get_all_vcs_roots', short_help='Get all vcs roots')
@common_options(_common_options)
@pass_context
def get_all_vcs_roots(ctx, server, port, auth_username, auth_password):
    """Get all vcs roots"""
    tc = TeamCity(auth_username, auth_password, server, port)
    tc.get_all_vcs_roots()


@cli.command('get_all_build_types', short_help='Get all build types')
@common_options(_common_options)
@pass_context
def get_all_build_types(ctx, server, port, auth_username, auth_password):
    """Get all build types"""
    tc = TeamCity(auth_username, auth_password, server, port)
    tc.get_all_build_types()


@cli.command('get_all_changes', short_help='Get all changes')
@common_options(_common_options)
@pass_context
def get_all_changes(ctx, server, port, auth_username, auth_password):
    """Get all changes"""
    tc = TeamCity(auth_username, auth_password, server, port)
    tc.get_all_changes()


@cli.command('get_server_info', short_help='Get server info')
@common_options(_common_options)
@pass_context
def get_server_info(ctx, server, port, auth_username, auth_password):
    """Get server info"""
    tc = TeamCity(auth_username, auth_password, server, port)
    tc.get_server_info()


@cli.command('get_agents', short_help='Get agents')
@common_options(_common_options)
@pass_context
def get_agents(ctx, server, port, auth_username, auth_password):
    """Get agents"""
    tc = TeamCity(auth_username, auth_password, server, port)
    tc.get_agents()


@cli.command('get_all_plugins', short_help='Get all plugins')
@common_options(_common_options)
@pass_context
def get_all_plugins(ctx, server, port, auth_username, auth_password):
    """Get all plugins"""
    tc = TeamCity(auth_username, auth_password, server, port)
    tc.get_all_plugins()
